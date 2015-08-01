import sys
from PIL import Image
def compress_image(source_pic, dest_pic, percentage):
    src_img = Image.open(source_pic)
    src_img.save(dest_pic, 'JPEG', quality=int(percentage))
if __name__ == "__main__":
    source_pic = sys.argv[1]
    dest_pic = sys.argv[2]
    percentage = sys.argv[3]
    compress_image(source_pic, dest_pic, percentage)
