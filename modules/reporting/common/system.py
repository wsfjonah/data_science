import reporting.common.config4me as config


def get_curr_proj():
    curr_proj = config.get_config('System', 'system.project.current')
    return curr_proj
