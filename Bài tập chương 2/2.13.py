import requests

response = requests.get('https://jsonplaceholder.typicode.com/comments?postId=1')

if response.status_code == 200:
    
    json_data = response.json()

    comments = json_data[:3]

    for i, j in enumerate(comments, start=1):
        print("Bình luận:",i)
        print("ID bài đăng:", j['id'])
        print("Tên:", j['name'])
        print("Email:", j['email'])
        print("Nội dung:", j['body'])
        print()

else:
    print("Không thể truy cập,.")