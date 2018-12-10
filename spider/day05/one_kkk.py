import requests
import random
import os
from PIL import Image
from compare_helper import get_compare
url = 'http://www.1kkk.com/image3.ashx?t=' + str(random.randint(0,1000))

def get_imgs():
    img_list = os.listdir('./images/')
    i = 0
    for path in img_list:
        i += 1
        img_path = './images/' + path
        Crop_imgs(img_path,i)
    return img_list

def Crop_imgs(img_path,i):

    image = Image.open(img_path)
    img_name = str(i)

    small_img = image.crop((0,0,76,76))
    small_img.save('./crop_img/' + img_name + 'first.png')
    small_img2 = image.crop((76, 0, 152, 76))
    small_img2.save('./crop_img/' + img_name + 'second.png')
    small_img3 = image.crop((152,0,228,76))
    small_img3.save('./crop_img/' + img_name + 'third.png')
    small_img4 = image.crop((228, 0, 304, 76))
    small_img4.save('./crop_img/' + img_name + 'fourth.png')

def Compare():
    small_list = os.listdir('./crop_img/')
    for i in range(len(small_list)-1):
        for j in range(i-1):
            filename1 = f'./crop_img/{small_list[i]}'
            filename2 = f'./crop_img/{small_list[j]}'
            compare = get_compare(filename1, filename2)
            if compare > 60:
                os.remove()
            print(compare)
# def get_resource(url):
#     headers = {
#         "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"
#     }
#
#     response = requests.get(url, headers=headers)
#
#     if response.status_code == 200:
#         return response.content
#     return None
#
#
def main():
    Compare()
    # get_imgs()
#     for i in range(300):
#         images = get_resource(url)
#         file_name = str(i) + '.jpg'
#         with open('./images/%s' % file_name,'wb') as f:
#             f.write(images)

if __name__ == '__main__':
    main()
