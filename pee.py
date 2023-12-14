import re, time
import requests, json
import pandas as pd
import vip
import os
import glob

duong_dan_thu_muc = r'E:\shopee'
danh_sach_excel = glob.glob(os.path.join(duong_dan_thu_muc, '*.xlsx')) # type: ignore
danh_sach = [os.path.splitext(os.path.basename(duong_dan))[0] for duong_dan in danh_sach_excel]

def price_sale(price, discount):
    price_sale = price - round(price*(discount/100), -3)
    return int(price_sale)

def format_string(input_string):
    result = re.sub(r'[^a-zA-Z0-9À-Ỹà-ỹẠ-Ỵạ-ỵĂ-Ắă-ằẤ-Ấấ-ấẦ-Ầầ-ầẨ-Ẩẩ-ẩẪ-Ẫẫ-ẫẬ-Ậậ-ậẮ-Ằắ-ắẲ-Ẳẳ-ẳẴ-Ẵẵ-ẵẶ-Ặặ-ặĨ-ĩỈ-ỉỊ-ịỌ-ỏỘ-ộỘ-ổ-Ở-ởỠ-ỡỢ-ợƠ-Ớơ-ớỜ-ờỚ-ỚỜ-ỜỞ-Ởở-ởỠ-Ỡỡ-ỡỢ-ỢỤ-ụỦ-ủỨ-ứỪ-Ừừ-ừỬ-Ửử-ửỮ-Ữữ-ữỰ-ựÝ-Ỳý-ỳỴ-ỴỶ-ỶỸ-Ỹ- -.-,-[-]-(-)]', ' ', input_string)
    return result

def get_shop_location(shopid):

    url = f"https://shopee.vn/api/v4/product/get_shop_info?shopid={shopid}"

    payload = {}
    headers = {
            'if-none-match-': '55b03-04c5bdaf20c828eb55cb80722d3c1345',
            'x-api-source': 'rweb',
            'x-kl-ajax-request': 'Ajax_Request',
            'x-requested-with': 'XMLHttpRequest',
            'x-shopee-language': 'vi',
            'Cookie': 'REC_T_ID=dada1132-35d2-11ee-b8d2-4e479a5f615d; SPC_EC=dWpNNVNkMldqZ1JxS2JDN5AxWG/KUrEWrJFNeNREdw4rbIgO7VSNnltihPnxKmNFScZ0Vtlyc6mBfLzK+Bk2XVQodwINgdIhzPnGNJ/PshCxRTB9Dh8UJd4sCRezXSRt4E7BAv7Nmj6K6kll7LlElLJFe3E+G1XRnk4c1LdwoU4=; SPC_F=1TiqVGU9Y15i74yzpbiFC76dTkxwKSxQ; SPC_R_T_ID=LDnfdJem78/ucqjboaO2xzTWjUwggLM5snzSLwM7G9fNqembLKqfSdpc98vqT10mwrXHml9aNoMKmsA0dfTaTgocDSv0CEvPxAhwb5ZDbGO/LljkgN8qmxHDrs57JD/cel5KgeofQnpcghDQnPOZJ85RN1XkBdbU5AA04BhxVdw=; SPC_R_T_IV=V3hVQjZza1Bid0d5S1R0TA==; SPC_SEC_SI=v1-eGx3RGROejZnd1U3MGdKR1GMsedddpoWpGIfOuZtAAGk9lHPozCvBOtRgq4V4UtH5XidsWnTpbK7BKM3NtDV+KXJfbMFMY0UEIQF6WDgPf4=; SPC_SI=YkdTZQAAAAAxVU9FQ09XaofuHgAAAAAAdmhGaE5SdjA=; SPC_ST=.aGZIWWgxQlQ3TVUyVW5tN5cjr1uhaQ1NXz9IaRE5RipTxgkmZU+3D956rORLSDkeUZt7b7gfpIjP7ZAbhmLScPgCvsfUSg4Nda9NyPLDtr0dP2ecuBij53UQ8F5vii5Nvg74r/z/PhsNul/9XgZwuyf8Y+CAQ3mVa7mlEi0UYCOZZrKhxR6WM/IEwANur6kP0sume3b0pqkFiOdZyNMQ+Q==; SPC_T_ID=LDnfdJem78/ucqjboaO2xzTWjUwggLM5snzSLwM7G9fNqembLKqfSdpc98vqT10mwrXHml9aNoMKmsA0dfTaTgocDSv0CEvPxAhwb5ZDbGO/LljkgN8qmxHDrs57JD/cel5KgeofQnpcghDQnPOZJ85RN1XkBdbU5AA04BhxVdw=; SPC_T_IV=V3hVQjZza1Bid0d5S1R0TA==; SPC_U=177993892'
    }

    try:
        
        response = requests.request("GET", url, headers=headers, data=payload)
        return json.loads(response.text)['data']['shop_location']
    except: return ''


def get_all_sessions():
    url = "https://shopee.vn/api/v4/flash_sale/get_all_sessions?category_personalization_type=1&tracker_info_version=0"
    sessions = []
    payload = {}
    headers = {
            'authority': 'shopee.vn',
            'accept': '*/*',
            'accept-language': 'vi,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
            'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
            'x-api-source': 'pc',
            'x-requested-with': 'XMLHttpRequest',
            'x-shopee-language': 'vi'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    data = response.json()['data']['sessions']
    for i in data:
        name = i['name']
        print(f'Session: {i["promotionid"]} - {name}')
        sessions.append({'promotionid': i['promotionid'], 'name': name})
    # print(sessions)
    return sessions

def get_all_item_session(session):
    url = f"https://shopee.vn/api/v4/flash_sale/get_all_itemids?need_personalize=true&promotionid={session}&sort_soldout=true&tracker_info_version=0"
    results = []
    payload = {}
    headers = {
            'authority': 'shopee.vn',
            'accept': '*/*',
            'accept-language': 'vi,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
            'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
            'x-api-source': 'pc',
            'x-requested-with': 'XMLHttpRequest',
            'x-shopee-language': 'vi'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    data = response.json()['data']['item_brief_list']
    for i in data:
        catid = i['catid']
        itemid = i['itemid']
        results.append({'session': session,'catid': catid, 'itemid': itemid})
        # break
    # print(results)
    return results

def get_info_item(session, itemid, catid):
    url = "https://shopee.vn/api/v4/flash_sale/flash_sale_batch_get_items"
    payload = json.dumps({
    "promotionid": session,
    "categoryid": catid,
    "itemids": [itemid],
    "limit": 16,
    "with_dp_items": True
    })
    headers = {
            'authority': 'shopee.vn',
            'accept': 'application/json',
            'accept-language': 'vi,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
            'content-type': 'application/json',
            'origin': 'https://shopee.vn',
            'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
            'x-api-source': 'pc',
            'x-requested-with': 'XMLHttpRequest',
            'x-shopee-language': 'vi'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    data = response.json()['data']['items'][0]
    shopid = data['shopid']
    shop_location = get_shop_location(shopid)
    link = vip.short(shopid,itemid)['shortlink']
    time.sleep(1)
    # link = f'https://shopee.vn/product/{shopid}/{itemid}'
    is_shop_official = data['is_shop_official']
    is_shop_preferred = data['is_shop_preferred']
    if is_shop_official == True and is_shop_preferred == False: shop_type = 'Mall'
    elif is_shop_preferred == True and is_shop_official == False: shop_type = 'Yêu thích'
    else: shop_type = 'Thường'
    price_before_discount = int(data['price_before_discount']/100000)
    raw_discount = data['raw_discount']
    price = price_sale(price_before_discount, raw_discount)
    name = format_string(data['name'])
    stock = data['stock']
    voucher_code = data['voucher']['voucher_code']
    promo_images = f"https://down-vn.img.susercontent.com/file/{data['promo_images'][0]}"
    reminder_count = data['reminder_count']
    return {'shop_location': shop_location, 'shopid': shopid, 'itemid': itemid, 'shop_type': shop_type, 'price_before_discount': price_before_discount, 'raw_discount': raw_discount, 'price': price, 'name': name, 'stock': stock, 'link': link, 'voucher_code': voucher_code, 'promo_images': promo_images, 'reminder_count': reminder_count}
    # print(f'Name: {name}\nStock: {stock}\nPrice: {price}\n\n')

import concurrent.futures


def process_item(item):
    try:
        info = get_info_item(item['session'], item['itemid'], item['catid'])
        print(f'{item}')

        return {
            'Loại shop': info['shop_type'],
            'Ảnh':' ',
            'Tên sản phẩm': info['name'],
            'Link': info["link"],
            'Giá Flash sale': info['price'],
            'Giá gốc': info['price_before_discount'],
            'Giảm (%)': info['raw_discount']/100,
            'Số lượng': info['stock'],
            'Voucher': info['voucher_code'],
            'Địa chỉ shop': info['shop_location'],
            'Lượt nhắc': info['reminder_count'],
            'Hình ảnh': info['promo_images']
        }
    except Exception as e:
        print(f"Error processing item: {e}")
        return None

def run(session, name):
    items = get_all_item_session(session)
    print(len(items))
    data_list = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(process_item, items))

    for result in results:
        if result is not None:
            data_list.append(result)
            # break

    data = pd.DataFrame(data_list)

    data.to_excel(f'E:\\shopee\\{name}.xlsx', index=False)

    print(f'Done! {len(data_list)} items')

for i in get_all_sessions():
    # print(danh_sach)
    if i['name'] in danh_sach: continue
    print(f'{i["name"]}')
    run(i['promotionid'], i['name'])

# run(189987593342979, 'Flash Sale Mon 11.12 21H - 24H')
# get_all_sessions()
    

