def sort_func(a, b, c, d, e, f, g, h, i, j, k ,l): # xml 태그 제거 func

    a_fix = '<root>{}</root>'.format(a)
    a_content = ET.fromstring(a_fix).text

    b_fix = '<root>{}</root>'.format(b)
    b_content = ET.fromstring(b_fix).text
    
    c_fix = '<root>{}</root>'.format(c)
    c_content = ET.fromstring(c_fix).text

    d_fix = '<root>{}</root>'.format(d)
    d_content = ET.fromstring(d_fix).text

    e_fix = '<root>{}</root>'.format(e)
    e_content = ET.fromstring(e_fix).text

    f_fix = '<root>{}</root>'.format(f)
    f_content = ET.fromstring(f_fix).text

    g_fix = '<root>{}</root>'.format(g)
    g_content = ET.fromstring(g_fix).text

    h_fix = '<root>{}</root>'.format(h)
    h_content = ET.fromstring(h_fix).text

    i_fix = '<root>{}</root>'.format(i)
    i_content = ET.fromstring(i_fix).text

    j_fix = '<root>{}</root>'.format(j)
    j_content = ET.fromstring(j_fix).text

    k_fix = '<root>{}</root>'.format(k)
    k_content = ET.fromstring(k_fix).text

    l_fix = '<root>{}</root>'.format(l)
    l_content = ET.fromstring(l_fix).text
    
    result = f"특허명 : {a_content}", f"IPC : {b_content}", f"출원인 : {c_content}", f"출원번호 : {d_content}", f"출원일자 : {e_content}", f"등록번호 : {f_content}", f"등록일자 : {g_content}", f"공개번호 : {h_content}", f"공개일자 : {i_content}", f"대리인 : {j_content}", f"발명자 : {k_content}",f"요약 : {l_content}", "\n"
    return result


# 키프리스 상세설명 태그 목록
""" 
tlv = item.find('tlv').text # 특허명
ipv = item.select_one('a').text # IPC
apv = item.find('apv').text # 출원인
vdkvgwkey = item.find('vdkvgwkey').text # 출원번호
adv = item.find('adv').text # 출원일자
gnv = item.find('gnv').text # 등록번호
gdv = item.find('gdv').text # 등록일자
onv = item.find('onv').text # 공개번호
odv = item.find('odv').text # 공개일자
agv = item.find('agv').text # 대리인
inv = item.find('inv').text # 발명자
abv = item.find('abv').text # 요약
"""