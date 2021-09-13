from PIL import Image
import os # ファイルやフォルダ操作
dir_name = "mikakou" # 画像が入っているフォルダ
Home_dir_name = "Home" # ホーム画面用の画像を保存する先のフォルダ
Lock_dir_name = "Lock" # ロック画面用の画像を保存する先のフォルダ

def add_margin(pil_img, top, right, bottom, left, color): # 余白をつける関数
  width, height = pil_img.size
  new_width = width + right + left
  new_height = height + top + bottom
  result = Image.new(pil_img.mode, (new_width, new_height), color)
  result.paste(pil_img, (left, top))
  return result

def expand2square(pil_img, background_color): # 正方形にする関数
  width, height = pil_img.size
  if width == height:
    return pil_img
  elif width > height:
    result = Image.new(pil_img.mode, (width, width), background_color)
    result.paste(pil_img, (0, (width - height) // 2))
    return result
  else:
    result = Image.new(pil_img.mode, (height, height), background_color)
    result.paste(pil_img, ((height - width) // 2, 0))
    return result

files = os.listdir(dir_name)

for file in files: # ホーム画面用の処理
  im = Image.open(os.path.join(dir_name, file))
  im_new = expand2square(im, (255, 255, 255))
  im_new = add_margin(im_new, 141+50, 64, 141+30, 64, (255, 255, 255))
  im_new.save(os.path.join(Home_dir_name, file))

for file in files: # ロック画面用の処理
  im = Image.open(os.path.join(dir_name, file))
  im_new = add_margin(im, 141+410, 0, 0, 0, (255, 255, 255))
  im_new.save(os.path.join(Lock_dir_name, file))