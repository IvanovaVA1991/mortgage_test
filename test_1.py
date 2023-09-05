from testsite import OperationsHelper
import time
import yaml


with open('./testdata.yaml', encoding='utf-8') as f:
	testdata = yaml.safe_load(f)


def test_form_positive_1(browser):
	testpage = OperationsHelper(browser)
	res = []
	for i in range(1, testdata['count_pos']+1):
		testpage.go_to_site()
		testpage.enter_sum(float(testdata.get(i).split(', ')[0]))
		time.sleep(1)
		testpage.enter_age(int(testdata.get(i).split(', ')[1]))
		time.sleep(1)
		testpage.object_choice(testdata.get(i).split(', ')[2])
		time.sleep(1)
		testpage.sex_choice(testdata.get(i).split(', ')[4])
		time.sleep(1)
		testpage.bank_choice(int(testdata.get(i).split(', ')[3]))
		time.sleep(1)
		try:
			testpage.click_count_button()
			time.sleep(2)
			if testpage.get_choice_text() == 'Выбор предложения':
				res.append(f"{i}: Pass, ")
			else: res.append(f"{i}: Fail, ")
		except:
			res.append(f"{i}: Fail, ")
			continue
	with open('res_file', 'a', encoding='utf-8') as file:
			file.write(f'TEST_POSITIVE: {res} \n')
	for item in res:
		assert 'Fail' not in item

