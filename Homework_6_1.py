with open('nginx_logs.txt', 'r', encoding='utf-8') as log_file:
    for my_file in log_file:
        set_my_file = my_file.split(sep=' ')
        remote_ip = set_my_file[:1]
        request_type = set_my_file[5:6]
        requested_resource = set_my_file[6:7]
        my_result = (*remote_ip, *request_type, *requested_resource)
        print(*my_result)
