def name_splitter(full_name):
  full_name = full_name.split(" ")
  first_name = ""
  if len(full_name)==1:
    first_name = full_name[0]
  else:
    for i in range(len(full_name)-1):
      first_name = first_name + full_name[i] + " "
  first_name = first_name.strip()
  last_name = full_name[-1]
  return first_name, last_name


from pathlib import Path
from django.core.files.storage import default_storage
from django.utils.text import slugify


def titled_upload_to(instance, filename, folder, title):
  extension = Path(filename).suffix.lower()
  base_name = slugify(title) or slugify(Path(filename).stem) or 'upload'
  candidate = f'{folder}/{base_name}{extension}'
  suffix = 1

  while default_storage.exists(candidate):
    candidate = f'{folder}/{base_name}-{suffix}{extension}'
    suffix += 1

  return candidate


def item_image_upload_to(instance, filename):
  return titled_upload_to(instance, filename, 'decorations/items', instance.Title)


def package_image_upload_to(instance, filename):
  return titled_upload_to(instance, filename, 'decorations/packages', instance.title)


def profile_picture_upload_to(instance, filename):
  return titled_upload_to(instance, filename, 'client/profile_pictures', instance.user.username)


def upload_to(instance, filename):
  owner_title = (
    instance.package.title if instance.package
    else instance.item.Title if instance.item
    else 'package-detail'
  )
  folder = 'decorations/packages/other'
  if instance.media_type == 'image':
    folder = 'decorations/packages/img'
  elif instance.media_type == 'video':
    folder = 'decorations/packages/video'
  return titled_upload_to(instance, filename, folder, owner_title)


from django.utils import timezone  
from datetime import timedelta 
def get_default_available_to():
    return timezone.now() + timedelta(days=30)