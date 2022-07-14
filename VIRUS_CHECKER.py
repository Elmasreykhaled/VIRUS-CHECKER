import requests
import json
import validators



def main():
    shape("     <<VIRUS_CHECKER>>     ")
    api_key = '30a0394aec16f5f15e877bd414011236dc7c43c07adedf591a91aa1d88a88a0f'
    counter = 0
    chooses = ["Domain", "IP", "URL"]
    while True:
        user_input = input("Please Enter URL OR Domain OR IP OR File Hash\n>> ")
        cheaking_result = check(user_input)
        if cheaking_result == "Domain":
            final_user_input = "https://" + user_input
        elif cheaking_result == "IP":
            final_user_input = "http://" + user_input
        else:
            final_user_input = user_input
        if cheaking_result in chooses:
            prams = {'apikey': api_key, 'resource': final_user_input}
            URL = 'https://www.virustotal.com/vtapi/v2/url/report'
            res = requests.get(URL, params=prams)
            res_json = json.loads(res.content)
            try:
                if res_json['positives'] > 0:
                    print(
                        f"\nThe Type is >>>>>>> {cheaking_result} \n'{user_input}' is >>>>>>>  Milicious\n")
                    break
                elif res_json['positives'] <= 0:
                    print(
                        f"\nThe Type is >>>>>>> {cheaking_result} \n \n'{user_input}' is >>>>>>>  Clean\n")
                    break
            except:
                print("You don't Input correct Value Please Try again")
        elif cheaking_result == "File_Hash":
            url = 'https://www.virustotal.com/vtapi/v2/file/report'
            params = {'apikey': api_key, 'resource': final_user_input}
            response = requests.get(url, params=params)
            res_json = json.loads(response.content)
            try:
                if res_json['positives'] > 0:
                    print(
                        f"\nThe Type is >>>>>>> {cheaking_result} \n \n'{user_input}' is >>>>>>>  Milicious\n")
                    break
                elif res_json['positives'] <= 0:
                    print(
                        f"\nThe Type is >>>>>>> {cheaking_result} \n'{user_input}' is >>>>>>>  Clean\n")
                    break
            except:
                print("\n>You don't Input correct Value Please Try again<\n")
        counter += 1
        if counter == 2 or counter == 4:
            quit_option = input("To quit Please Enter (q) to continue (any another key)\n>>>>")
            if quit_option.lower() == "q":
                break
        elif counter > 4:
            print("\nOut of Rtying, Please Make sure about the input and try again later\n")
            break

    print("Thank You For Using <<VIRUS_CHECKER>>\n")


def shape(text):
    name = len(text)
    num = int(5)
    for i in range(num):
        if i == 0 or i == num - 1:
            print('*' * (name + 2))
        elif i == int(num / 2):
            print('*' + text + '*')
        else:
            print('*' + ' ' * name + '*')

def check(user_input):
    if_domain = validators.domain(user_input)
    if if_domain is True:
        return "Domain"
    else:
        if_ipv4 = validators.ipv4(user_input)
        if_ipv6 = validators.ipv6(user_input)
        if if_ipv4 is True or if_ipv6 is True:
            return "IP"
        else:
            if_url = validators.url(user_input)
            if if_url is True:
                return "URL"
            else:
                return "File_Hash"



if __name__ == '__main__':
    main()

