import os
from django.db import models
from django.contrib import admin
from gallery.settings import MEDIA_ROOT
from django.db.models.fields.files import ImageFieldFile
import Image

def make_thumb(path, size = 240):
    pixbuf = Image.open(path)
    width, height = pixbuf.size

    if width > size:
        delta = width / size
	height = int(height / delta)

    pixbuf.thumbnail((size, height), Image.ANTIALIAS)
    return pixbuf


class Pic(models.Model):
    headImg = models.FileField(upload_to = 'img')
    thumImg = models.FileField(upload_to = 'img', blank = True)

    def save(self):
	super(Pic, self).save()
	base, ext = os.path.splitext(os.path.basename(self.headImg.path))
	thumb_pixbuf = make_thumb(os.path.join(MEDIA_ROOT, self.headImg.name))
	relate_thumb_path = os.path.join('img', base + '.thumb' + ext)
	thumb_path = os.path.join(MEDIA_ROOT, relate_thumb_path)
	thumb_pixbuf.save(thumb_path)
	self.thumImg = ImageFieldFile(self, self.thumImg, relate_thumb_path)
	super(Pic, self).save()


class PicAdmin(admin.ModelAdmin):
    list_display = ('headImg', 'thumImg')

    def log_deletion(self, request, object, object_repr):
	super(PicAdmin, self).log_deletion(request, object, object_repr)
	os.system("rm %s %s -rf" % (object.headImg.path, object.thumImg.path))


admin.site.register(Pic, PicAdmin)
