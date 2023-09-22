from bs4 import BeautifulSoup
import requests
import pandas

URL = "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors"

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")
# print(soup)

pagination = soup.select(".pagination__btn--inner")
page_count = int(pagination[5].text)

data = []

for page in range(1, page_count + 1):
	url = URL + f"/page/{page}"
	response = requests.get(url)
	soup = BeautifulSoup(response.text, "html.parser")

	table_rows = soup.findAll("tr", {"class": "data-table__row"})

	for row in table_rows:
		cells_data = row.findChildren("span", {"class": "data-table__value"})
		row_data = {
			"Undergraduate Major": cells_data[1].text,
			"Starting Median Salary": float(cells_data[3].text.strip("$").replace(",", "")),
			"Mid-Career Median Salary": float(cells_data[4].text.strip("$").replace(",", ""))
		}
		data.append(row_data)
print(data)

pandas.DataFrame(data).to_csv("new_salaries_by_college_major.csv", index=False)
