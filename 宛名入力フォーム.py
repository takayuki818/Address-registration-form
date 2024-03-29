import PySimpleGUI as sg
import os
def レイアウト作成(data):
    layout = [
        [sg.Text('氏　　名'), sg.InputText(key='name',size=(20))],
        [sg.Text('郵便番号'), sg.InputText(key='post_code',size=(20))],
        [sg.Text('住　　所'), sg.InputText(key='address',size=(20))],
        [sg.Button('追加'), sg.Button('削除')],
        [sg.Listbox(values=data, size=(30, 10), key='list')],
        [sg.Button('保存'), sg.Button('終了')]
    ]
    return layout

def main():
    data = [] # 宛名データを保持するリスト
    window = sg.Window('封筒宛名管理', レイアウト作成(data))
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == '終了':
            break
        elif event == '追加':
            name = values['name']
            post_code = values['post_code']
            address = values['address']
            if name and post_code and address:
                data.append([name,post_code,address])
                window['list'].update(values=data)
                for key in ['name','post_code','address']:
                    window[key].update('')
        elif event == '削除':
            selected_index = window['list'].get_indexes()
            if selected_index:
                del data[selected_index[0]]
                window['list'].update(values=data)
        elif event == '保存':
            with open('宛名台帳.txt', 'w') as file:
                for row_data in data:
                    file.write(','.join(row_data) + '\n')
    window.close()
if __name__ == '__main__':
    main()
