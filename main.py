from utils import get_triangle_area 
from bs4 import BeautifulSoup
from requests import get

def main():
    a = 3;
    h = 6;
    req = get("https://www.day.az")
    print(req.text)
    res = get_triangle_area(a, h) 
    print(res) 
    print('this is new added message')

if __name__ == "__main__":
    main()
