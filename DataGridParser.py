debug = False

html = '''
<mx:AdvancedDataGridColumn headerText="대표자명"    dataField="rpreenam" sortable="false" width="60" textAlign="center"/>
'''.strip()
print(html)

html = html.replace('<', '').replace('/>', '')

data = {}
for i, parsed in list(enumerate(html.split())):
    a = parsed.split('=')

    # print(a)
    if a[0] == 'mx:AdvancedDataGridColumn':
        data['isAdvancedDataGridColumn'] = True
    if len(a) == 1:
        continue
    a[0] = a[0].strip('"')
    a[1] = a[1].strip('"')

    data[a[0]] = a[1]

if debug:
    print('//', data)

out = "new ColBuilder([ '{}', '{}' ], '{}')".format( 
    data['headerText'],
    data['headerText'],
    data['dataField'])
out1 = "Width: {}, Align: '{}', CanSort: {}".format(
    data['width'],
    data['textAlign'].capitalize(),
    1 if data['sortable'] == 'true' else 0
)
print(out + ".setProp({ " + out1 + " }).build(),")
