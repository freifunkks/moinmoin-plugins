# Borrowed some code from ShowCSV:
# https://moinmo.in/MacroMarket/ShowCSV

import codecs
import os
import yaml

from MoinMoin import config
from MoinMoin.action import AttachFile

def utf_8_encoder(unicode_csv_data):
    for line in unicode_csv_data:
        yield line.encode('utf-8')

def get_yaml(file, attach_dir):
    return yaml.load(codecs.open(os.path.join(attach_dir, file), 'rb', config.charset))

def macro_FFImageChooser(macro):
    channels_file = 'channels.yml'
    vendors_file = 'vendors.yml'

    request = macro.request
    formatter = macro.formatter

    pagename = formatter.page.page_name
    files = AttachFile._get_files(request, pagename)
    attach_dir = AttachFile.getAttachDir(request, pagename)

    # channels
    try:
        channels_idx = files.index(channels_file)
    except ValueError:
        return "Konnte Dateianhang " + channels_file +" nicht finden"
    channels = get_yaml(files[channels_idx], attach_dir)

    # vendors
    try:
        vendors_idx = files.index(vendors_file)
    except ValueError:
        return "Konnte Dateianhang " + vendors_file + " nicht finden"
    vendors = get_yaml(files[vendors_idx], attach_dir)

    # output
    ret = '<form action="/download/" class="download-form">'
    for vendor in vendors:
        ret += """
<input type="radio" name="vendor" value="%(id)s" class="vendor" id="vendor-%(id)s" />
    <label for="vendor-%(id)s">%(name)s</label>
    <div class="device-list">
               """ % vendor
        for device in vendor['devices']:
            ret += '''
        <div class="device-wrap">
          <input type="radio" name="device" value="%(device_id)s" class="device" id="device-%(vendor_id)s-%(device_id)s" />
          <label for="device-%(vendor_id)s-%(device_id)s">
            %(device_name)s
          </label>
          <div class="versions">
                   ''' % {'device_id': device['id'], 'device_name': device['name'], 'vendor_id': vendor['id']}
            try:
                versions = device['versions']
            except:
                versions = ''
                pass
            for version in versions:
                try:
                    version_label = version['name']
                except:
                    version_label = version['id']
                    pass
                ret += '''
                <input type="radio" name="version" value="%(version_id)s" class="version" id="version-%(vendor_id)s-%(device_id)s-%(version_id)s" />
                <label for="version-%(vendor_id)s-%(device_id)s-%(version_id)s">%(version_label)s</label>
                       ''' % {'device_id': device['id'], 'vendor_id': vendor['id'], 'version_id': version['id'], 'version_label' : version_label}
            ret += '''
          </div>
        </div>
                   '''

        ret += '''
    </div>
</input>
               '''
    for channel in channels:
        ret += '<button type="submit" class="download-button">%(name)s herunterladen</button>' % channel

    return ret

