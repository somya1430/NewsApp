import requests
import time

country = { 1:'ae' ,2:'ar' ,3:'at' ,4:'au' ,5:'be' ,6:'bg' ,7:'br' ,8:'ca' ,9:'ch' ,10:'cn' ,11:'co' ,12:'cu' ,13:'cz' ,14:'de' ,15:'eg' ,16:'fr' ,17:'gb' ,18:'gr' ,19:'hk' ,20:'hu' ,21:'id' ,22:'ie' ,23:'il' ,24:'in' ,25:'it' ,26:'jp' ,27:'kr' ,28:'lt' ,29:'lv' ,30:'ma' ,31:'mx' ,32:'my' ,33:'ng' ,34:'nl' ,35:'no' ,36:'nz' ,37:'ph' ,38:'pl' ,39:'pt' ,40:'ro' ,41:'rs' ,42:'ru' ,43:'sa' ,44:'se' ,45:'sg' ,46:'si' ,47:'sk' ,48:'th' ,49:'tr' ,50:'tw' ,51:'ua' ,52:'us' ,53:'ve' ,54:'za'}

nation = { 1:'UAE' ,2:'Argentina' ,3:'Austria' ,4:'Australia' ,5:'Belgium' ,6:'Bulgeria' ,7:'Brazil' ,8:'Canada' ,9:'Switzerland' ,10:'China' ,11:'Colombia' ,12:'Cuba' ,13:'Czech Republic' ,14:'Germany' ,15:'Egypt' ,16:'France' ,17:'United Kingdom' ,18:'Greece' ,19:'Hong Kong' ,20:'Hungary' ,21:'Indonesia' ,22:'Ireland' ,23:'Israel' ,24:'India' ,25:'Italy' ,26:'Japan' ,27:'South Korea' ,28:'LIthuania' ,29:'Latvia' ,30:'Marocco' ,31:'Maxico' ,32:'Malaysia' ,33:'Nigeria' ,34:'Netherlands' ,35:'Norway' ,36:'New Zealand' ,37:'Philippines' ,38:'Poland' ,39:'Portugal' ,40:'Romania' ,41:'Serbia' ,42:'Russia' ,43:'Saudi arabia' ,44:'Sweden' ,45:'Singapore' ,46:'Slovenia' ,47:'Solvakia' ,48:'Thiland' ,49:'Trukey' ,50:'Taiwan' ,51:'ukraine' ,52:'United State' ,53:'Venezuela' ,54:'South Africa'}

# Enter your own api key from news api. It's free and a open source
API_KEY = "api key"

# make your choice to get desired news
def url_(n):
    if n == 1:
        for c in nation:
            print(f"{c} = {nation[c]}")
        count = int(input("\nEnter the country serial no. : "))
        link = f"https://newsapi.org/v2/top-headlines?country={country[count]}&apiKey={API_KEY}"
    elif n ==2:
        topic = str(input("\nEnter your reuired topic"))
        date = time.strftime("%Y-%m-%d")
        link = f"https://newsapi.org/v2/everything?q={topic}&from={date}&sortBy=publishedAt&apiKey=7b60d3c760cc4f9ab0b767f02b9e5de5"
    return link

#Extract news
def news():
    while True:
        choice = int(input("0->When finish reading\n1-> News headlines of any country\n2->News on any specific topic\n"))
        if choice == 0:
            break
        elif choice<0 or choice>2:
            print("Invalid Choice")
        else:
            url = url_(choice)
        news = requests.get(url).json()
        article = news['articles']
        
        headline = []
        for head in article:
            headline.append(head['title'])
            
        print("\nHEADLINES...")
        for i in range(len(headline)):
            print (f"{i+1} -> {headline[i]}")
        print(len(headline))
        
        des = []
        for dsp in article:
            des.append(dsp['description'])
        content = []
        for cont in article:
            content.append(cont['content'])
        while True:
            no = int(input("\nFor details of any headlines enter the headline no. \nfor proceed to next news enter 0 : "))
            if (no == 0):
                break
            elif no<0 or no >len(headline):
                print("Invlaid choice")
                continue
            print(f"\nDescription = {des[no-1]}\ncontent = {content[no-1]}")

news()