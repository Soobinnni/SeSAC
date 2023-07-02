# total_page = 13  # 전체 페이지
# size = 3  # 화면에 노출할 최대 페이지 수

# # 함수
# def cut_list( list, n ) : # list는 전체 범위의 리스트 / n은 간격
#     return [list[ i : i + n ] for i in range( 0, len(list), n )]    

# total_page_list = list(range(1, total_page + 1))
# page_list = cut_list(total_page_list, size)
# print(total_page_list)
# print(page_list)

# cur_page = 5 #현재 페이지

# # 페이지의 페이지리스트 반환
# def cur(cur_page):
#     for page in page_list:
#         if cur_page in page:
#             return page

# print(cur(cur_page)) 
page_list = list(range(1, 14))

print(page_list)


result = [page_list [i:(i+3)] for i in range(0, len(page_list), 3)]
print(result)