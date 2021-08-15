import requests
import re


def get_current_temp():
    req = requests.get("http://www.hidmet.gov.rs/latin/osmotreni/index.php")
    content = str(req.text)
    city = "Beograd"
    pattern = f"{city}</td>"
    idx = content.find(pattern)
    idx += len(pattern)
    content = content[idx:]
    end_idx = content.find("</td>")
    start_idx = end_idx - 1
    char = content[start_idx]
    while(char != ">"):
        start_idx -= 1
        char = content[start_idx]
    current_temp = content[start_idx+2:end_idx]
    return current_temp


def get_min_and_max_temp():
    req = requests.get("http://www.hidmet.gov.rs/latin/prognoza/index.php")
    content = str(req.text)
    city = "Beograd"
    pattern = f"{city}</td>"
    idx = content.find(pattern)
    content = content[idx:]
    idx = content.find("</tr>")
    content = content[:idx]
    pattern = re.compile(">-{0,1}[0-9]+<")
    matches = pattern.findall(content)
    min_max_temp = f"{matches[1][1:-1]}°/{matches[2][1:-1]}°"
    return min_max_temp


if __name__ == "__main__":
    req = requests.get("http://www.hidmet.gov.rs/latin/osmotreni/index.php")
    content = str(req.text)
    degree_sign = u"\N{DEGREE SIGN}"
    current_temp = get_current_temp()
    min_and_max_temp = get_min_and_max_temp()
    print(f"{current_temp}{degree_sign}C [{min_and_max_temp}]")   
