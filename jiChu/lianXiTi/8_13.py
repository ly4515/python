def build_profile(first, last, **info):
    '''创建一个字典，包含用户信息
    两个星号，创建空字典'''
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in info.items():
        profile['key'] = value
    return profile


user_profile = build_profile('ying', 'liu', age='18', sex='nv')
print(user_profile)