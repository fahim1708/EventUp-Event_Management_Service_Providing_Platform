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


from os.path import splitext
def upload_to(instance, filename):
    # Determine the file extension
    ext = splitext(filename)[1].lower()

    # Define the upload path based on media type
    if instance.media_type == 'image':
        return f'decorations/packages/img/{filename}'
    elif instance.media_type == 'video':
        return f'decorations/packages/video/{filename}'
    else:
        return f'decorations/packages/other/{filename}'  # Fallback path if needed


from django.utils import timezone  
from datetime import timedelta 
def get_default_available_to():
    return timezone.now() + timedelta(days=30)