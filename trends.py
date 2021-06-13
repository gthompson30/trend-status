from pytrends.request import TrendReq

def status(term):
	pytrend = TrendReq(hl='en-US', tz=360)
	keywords = [term]
	
	pytrend.build_payload(
	     kw_list=keywords,
	     cat=0,
	     timeframe='2004-01-01 2029-06-01',
	     geo='TW',
	     gprop='')
	data = pytrend.interest_over_time()
	
	if list(data) == []:
		return -1
	
	popularity = list(data[term].array)
	last_point = popularity[-1]
	'''
	data= data.drop(labels=['isPartial'],axis='columns')
	image = data.plot(title = f'Historical Popularity of {term} from 2004 - present')
	fig = image.get_figure()
	fig.savefig('figure.png')
	'''
	return last_point / 100

'''
print('Tiktok:')
print(status('TikTok'))
print('Minecraft:')
print(status('Minecraft'))
print('Coronavirus:')
print(status('Coronavirus'))
print('COVID-19:')
print(status('COVID-19'))
print('Google:')
print(status('Google'))
print('Harambe:')
print(status('Harambe'))
print('Doge')
print(status('Doge'))
print('Pfizer:')
print(status('Pfizer'))
'''
