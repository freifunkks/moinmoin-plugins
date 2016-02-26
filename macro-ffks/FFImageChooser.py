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
    vendors_file = 'vendors.yml'

    # TODO: Add this to the yml file?
    release = 'v2016.1-1'

    request = macro.request
    formatter = macro.formatter

    pagename = formatter.page.page_name
    files = AttachFile._get_files(request, pagename)
    attach_dir = AttachFile.getAttachDir(request, pagename)

    # vendors
    try:
        vendors_idx = files.index(vendors_file)
    except ValueError:
        return "Konnte Dateianhang " + vendors_file + " nicht finden"
    vendors = get_yaml(files[vendors_idx], attach_dir)

    # output
    ret = '<div class="download-form">'

    for vendor in vendors:
        ret += '''
            <input type="radio" name="vendor" class="vendor" id="vendor-%(id)s" />
            <label for="vendor-%(id)s">%(name)s</label>
            <div class="device-list">''' % vendor

        for device in vendor['devices']:
            ret += '<div class="device-wrap">'

            if 'versions' in device:
                ret += '''
                    <input type="radio" name="device" class="device" id="device-%(vendor_id)s-%(device_id)s" />
                    <label for="device-%(vendor_id)s-%(device_id)s">%(device_name)s</label>
                    <div class="version-list">
                    ''' % {'device_id': device['id'], 'device_name': device['name'], 'vendor_id': vendor['id']}
                for version in device['versions']:
                    try:
                        version_label = version['name']
                    except:
                        version_label = version['id']

                    ret += '''
                        <a class="version" href="https://dl.freifunk-kassel.de/images/stable/factory/gluon-ffks-%(release)s-%(vendor)s-%(device)s-%(version)s.bin">
                            %(text)s
                        </a>''' % {'release': release, 'vendor': vendor['id'], 'device': device['id'], 'version': version['id'], 'text': version_label}

                ret += '</div>'
            else:
                ret += '''
                    <a class="device" href="https://dl.freifunk-kassel.de/images/stable/factory/gluon-ffks-%(release)s-%(vendor)s-%(device)s.bin">
                        %(text)s
                    </a>''' % {'release': release, 'vendor': vendor['id'], 'device': device['id'], 'text': device['name']}

            ret += '</div>'

        ret += '</div>'

    ret += '<script type="text/javascript" src="/wikistatic/ffks/js/firmware-dl.js"></script>'

    return ret
