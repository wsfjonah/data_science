import socketserver
import datetime
import json
import os
import traceback
import reporting.app.importer.bxru1_1_parser as parser
import reporting.common.log4me as log
import reporting.common.config4me as config

data_dir = config.get_config_default('File_Storage', 'fs.storage', '/var/data/rtu1.1/')
HOST, PORT = "0.0.0.0", 1603


class RTUTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        while True:
            data = []
            try:
                data = self.request.recv(1024*2)
                if len(data) < 17:
                    continue

                log.info("{} send_len: ".format(self.client_address[0]) + str(len(data)))
                # tmp_dir = os.path.join(data_dir, 'tmp')
                # os.makedirs(tmp_dir, 0o775, True)
                # tmp_file = os.path.join(tmp_dir, datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
                #                         + '.bin')
                # with open(tmp_file, 'wb') as f:
                #     f.write(data)
                #
                # rtu_data = parser.parse(tmp_file)

                rtu_data = parser.parse_by_bytes(data)
                log.info("rtu meta: ip: "+self.client_address[0]+", s_id: " + rtu_data['site_id']
                         + ", read_t: " + rtu_data['read_time']
                         + ", send_t: " + rtu_data['send_time']
                         # + ", JZXS: "+rtu_data['JZXS']
                         # + ", k: " + str(rtu_data['k'])
                         # + ", b: " + str(rtu_data['b'])
                         + ", len: " + str(len(rtu_data['data']))
                         + ", reading: " + str(rtu_data['data'][0])
                         )

                if not rtu_data['site_id'].startswith("00"):
                    raise Exception("Invalid site id: "+rtu_data['site_id'])

                out_file = open(os.path.join(data_dir,
                                             rtu_data['site_id'] + "_" + rtu_data['read_time'] + ".json"), "w+")

                out_file.write(json.dumps(rtu_data))
                out_file.close()

                ack = parser.generate_ack(data, rtu_data)
                log.info("ack: " + ack.hex())
                self.request.sendall(ack)
            except ConnectionResetError as e:
                print("err ", e)
                log.info("ConnectionResetError:" + str(e))
            except Exception as exception:
                error_fname = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f') + '.bin'
                log.info("Error data ("+error_fname+") Exception:" + str(exception))
                write_error_data(data, error_fname)
                exstr = traceback.format_exc()
                print(exstr)


def write_error_data(data, fname):
    err_dir = os.path.join(data_dir, 'err')
    os.makedirs(err_dir, 0o775, True)
    tmp_file = os.path.join(err_dir, fname)
    with open(tmp_file, 'wb') as f:
        f.write(data)


if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer((HOST, PORT), RTUTCPHandler)
    print('waiting for RTU connection ... at ' + str(PORT) + ' for ' + HOST)
    server.serve_forever()
