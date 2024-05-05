import requests
import plotly.express as px

#the api can be found at this link found it through github apis which is really cool! https://github.com/Hipo/university-domains-list
url = 'https://raw.githubusercontent.com/Hipo/university-domains-list/master/world_universities_and_domains.json'
r = requests.get(url)
print(f"status code: {r.status_code}")
universities = r.json()
university_names = []
country_names = []
web_pages = []
hover_texts = []
for university in universities[:30]:
    name = university['name']
    university_names.append(name)
    country = university['country']
    country_names.append(country)
    web_page = university['web_pages'][0] if university['web_pages'] else "N/A"
    web_pages.append(web_page)
    hover_texts.append(f"{name}, {country}")

titled = "Top 30 Universities Globally by Web Page visits"
labels = {'y': 'University Name', 'x': 'Web Page link'}
fig = px.bar(y=university_names, x=web_pages, title=titled, labels=labels, hover_data={'y': hover_texts}, orientation='h')
fig.update_layout(title_font_size=32, xaxis_title_font_size=25, yaxis_title_font_size=25)
fig.update_traces(marker_color='green')
fig.show()