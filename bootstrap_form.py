# Author Jody Fitzpatrick
# Hey it's free, and it --- well works a little bit right now but will work
# better in latter versions.

import requests
import json


def create_form(api_end_pont):

    response = requests.options(api_end_point)
    data = json.loads(response.text)

    print(len(data['actions']['POST']))

    my_dict = data['actions']['POST']

    key_list = list(my_dict.keys())
    val_list = list(my_dict.values())

    print(key_list)

    fields = []
    for key in key_list:

        field = dict()
        field['name'] = key
        field['type'] = my_dict[key]['type']
        field['required'] = my_dict[key]['required']
        field['read_only'] = my_dict[key]['read_only']
        field['label'] = my_dict[key]['label']
        field['max_length'] = my_dict[key]['max_length'] if 'max_length' in my_dict[key] else False
        field['position'] = ''  # my_dict[key]['position']
        fields.append(field)

    # build the form... old school.

    response = []
    response.append("<form action='%s' method='post' name='%s'>" %(api_end_point,data['name'].replace(' ','-')))
    for field in fields:
        
        field_type = 'text'

        if field['read_only']:
            field_type = 'hidden'

        response.append("<div class='form-group'>")
        response.append('' if not field['read_only'] else response.append("<label for='%s-form-input'>%s</label>"%(field['name'],field['label'])))
        form_input = "<input class='form-control' type='%s' id='%s-form-input' name='%s'>"%(field_type, field['name'], field['name'])
        response.append(form_input)
        response.append("</div>")

    response.append("</form>")
    return response


def render_form(form):
    
    rendered = ''
    for field in form:
        rendered = rendered + str(field)
    
    return rendered


api_end_point = "http://localhost:8000/v1/project/list/"
    
