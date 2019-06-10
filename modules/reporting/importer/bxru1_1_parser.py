import struct

import reporting.util.coding as coding


def generate_ack(data, parsed_data):
    ack = data[:10]
    ack = ack + bytes.fromhex("32800802")
    ack = ack + bytes.fromhex(parsed_data['sn'])
    ack = ack + bytes.fromhex(parsed_data['send_time'][2:])
    ack = ack + bytes.fromhex("04")
    # crc16_check = coding.crc16(str(ack), True)
    crc16_check = coding.crc16_modbus(ack.hex())
    print("crc16: " + crc16_check)
    while len(crc16_check) < 4:
        crc16_check = '0' + crc16_check

    checksum = bytes.fromhex(crc16_check)
    ack = ack + checksum
    return ack


def get_reading(binary_content):
    data = []
    for num in range(0, int((len(binary_content) - 3) / 2)):
        count = int('{:08b}'.format(binary_content[num * 2])[0:5], 2)
        d = int(('{:08b}'.format(binary_content[num * 2]) + '{:08b}'.format(binary_content[num * 2 + 1]))[-11:], 2) * 2
        for n in range(0, count):
            data.append(d)
        # print('data_length：', len(data))
    return data


def get_data_by_bytes(data_bytes):
    print(len(data_bytes))
    print(data_bytes)
    for num in range(0, int((len(data_bytes) - 3) / 2)):
        print(data_bytes[num])
        print(data_bytes[num + 1])
        print(data_bytes[num].hex())


def parse(file_path):
    rtu = {}

    f = open(file_path, "rb+")

    # 报头
    # 1		帧起始	2	0x7e7e
    start = f.read(2).hex()
    print('start:', start)  # 帧起始
    rtu['start'] = start
    # 2		设备唯一编号	8	BCD码
    site_id = f.read(8).hex()  # 设备唯一编号
    print('site_id:', site_id)
    rtu['site_id'] = site_id
    # 3		设备用户编号	5	BCD码
    f.read(5)
    # 4		功能码	1	定时报0x32
    print("function_code: " + f.read(1).hex())
    # 5		报文上下行标识及长度	2	*1
    data_len = f.read(2).hex()
    print('data_len:', data_len)
    # 6		报文起始符	1	STX/SYN。（0x02/0x22 ）
    f.read(1)
    # 7		包总数及序列号	3	报文起始符为SYN时编入该组，采用HEX码，高12位表示包总数，低12位表示本次发送数据包的序列号，范围为1～4095
    f.read(3)

    ##正文
    # 1	流水号	流水号	2字节HEX码，范围1～65535
    sn = f.read(2).hex()
    print('sn:', sn)
    rtu['sn'] = sn
    # 2	发报时间	发报时间	6字节BCD码，YYMMDDHHmmSS
    send_time = '20' + f.read(6).hex()
    print('send_time: ' + send_time)
    rtu['send_time'] = send_time

    # 3	观测时间	观测时间	6字节BCD码，YYMMDDHHmmSS
    read_time = '20' + f.read(6).hex()
    print('read_time: ' + read_time)
    rtu['read_time'] = read_time

    # 4	测站分类	测站分类	1字节
    f.read(1)

    # 5	模拟量校正系数	数据校正系数	矫正系数共16个字节。详见下。
    f.read(16)

    # 6	模拟量的量程	模拟量的量程	模拟量的量程共16个字节，定义见下
    f.read(16)

    # 7	模拟量采集频率	模拟量采集频率	模拟量采集频率8个字节，定义见下
    f.read(4)
    f.read(3)
    for i in f.read(1):
        rtu['frequency'] = i

    # 8	传感类型	传感类型	传感类型（电流/或电压）8个字节
    f.read(8)

    # 9	转发周期	转发周期	四字节 int 分钟为单位
    f.read(8)

    # 存储状态	存储状态	后跟4字节int Sdcard_Status_No_Useing = 0, //tf卡尚未使用
    # Sdcard_Status_Init_Fail,//初始化失败
    # Sdcard_Status_Init_Ok,//初始化成功
    # Sdcard_Status_Save_Fail,//写文件失败
    # Sdcard_Status_Save_OK//写文件成功
    init_status = f.read(8).hex()
    print('init_status:', init_status)
    rtu['init_status'] = init_status
    # 11	信号质量		后跟四字节 int 取值 0~99
    signal_qty = f.read(8).hex()
    print('signal_qty:', signal_qty)
    rtu['signal_qty'] = signal_qty

    # #################################数据#########################################
    # 12 模拟量采集原始数值	5秒内的模拟量采集值	多个Short型变量（2字节乘以n），每个short都是高字节在前。
    data = f.read()
    # print(len(data)-3)
    # print('{:08b}'.format(data[-3]),'{:08b}'.format(data[-3])[3:8],int('{:08b}'.format(data[-3])[3:8],2))

    # print(hex(data[-3]),hex(data[-2]),hex(data[-1]))
    rtu['data'] = get_reading(data)
    # print(chr(100),ord('A'))

    f.close()
    # print(ord(data)) #将二进制数据转化为10进制数据。

    return rtu


def parse_by_bytes(data):
    rtu = dict()
    # 报头
    # 1		帧起始	2	0x7e7e
    rtu['start'] = data[0:2].hex()
    # 2		设备唯一编号	8	BCD码
    rtu['site_id'] = data[2:10].hex()
    # 3		设备用户编号	5	BCD码
    rtu['user_id'] = data[10:15].hex()
    # 4		功能码	1	定时报0x32
    rtu['function_code'] = data[15:16].hex()
    # 5		报文上下行标识及长度	2	*1
    rtu['data_len'] = data[16:18].hex()
    # 6		报文起始符	1	STX/SYN。（0x02/0x22 ）
    rtu['data_start'] = data[18:19].hex()
    # 7		包总数及序列号	3	报文起始符为SYN时编入该组，采用HEX码，高12位表示包总数，低12位表示本次发送数据包的序列号，范围为1～4095
    rtu['sum&id'] = data[19:22].hex()

    # 正文,22字节开始
    # 1	流水号	流水号	2字节HEX码，范围1～65535
    rtu['sn'] = data[22:24].hex()
    # 2	发报时间	发报时间	6字节BCD码，YYMMDDHHmmSS
    rtu['send_time'] = '20' + data[24:30].hex()

    # 3	观测时间	观测时间	6字节BCD码，YYMMDDHHmmSS
    rtu['read_time'] = '20' + data[30:36].hex()

    # 4	测站分类	测站分类	1字节
    rtu['sort'] = data[36:37].hex()

    # 5	模拟量校正系数	数据校正系数	矫正系数共16个字节。详见下。
    rtu['JZXS'] = data[37:53].hex()
    rtu['k'] = struct.unpack('!f', bytes.fromhex(rtu['JZXS'][8:16]))[0]
    rtu['b'] = struct.unpack('!f', bytes.fromhex(rtu['JZXS'][-8:]))[0]

    # 6	模拟量的量程	模拟量的量程	模拟量的量程共16个字节，定义见下
    rtu['MNLC'] = data[53:69].hex()

    # 7	模拟量采集频率	模拟量采集频率	模拟量采集频率8个字节，定义见下
    rtu['frequency'] = data[69:77].hex()

    # 8	传感类型	传感类型	传感类型（电流/或电压）8个字节
    rtu['CGLX'] = data[77:85].hex()

    # 9	转发周期	 int 分钟为单位 共8字节
    rtu['ZFZQ'] = data[85:93].hex()

    # 10 存储状态	存储状态	后跟4字节int Sdcard_Status_No_Useing = 0, //tf卡尚未使用
    # Sdcard_Status_Init_Fail,//初始化失败
    # Sdcard_Status_Init_Ok,//初始化成功
    # Sdcard_Status_Save_Fail,//写文件失败
    # Sdcard_Status_Save_OK//写文件成功
    rtu['init_status'] = data[93:101].hex()

    # 11	信号质量		后跟四字节 int 取值 0~99 共8字节
    rtu['signal_qty'] = data[101:109].hex()

    # #################################数据#########################################
    # 12 模拟量采集原始数值	5秒内的模拟量采集值	多个Short型变量（2字节乘以n），每个short都是高字节在前。
    data = data[109:]
    rtu['data'] = get_reading(data)

    # 结束字符
    rtu['end'] = data[-3:].hex()
    return rtu
