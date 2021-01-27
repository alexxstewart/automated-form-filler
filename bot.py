from splinter import Browser
import time

button1Path = 'div[class="appsMaterialWizToggleRadiogroupElContainer exportContainerEl  docssharedWizToggleLabeledControl freebirdThemedRadio freebirdThemedRadioDarkerDisabled"]:nth-child(2)'

button = 'div[id="i11"]'

submitButton = 'div[class="appsMaterialWizButtonEl appsMaterialWizButtonPaperbuttonEl appsMaterialWizButtonPaperbuttonFilled freebirdFormviewerViewNavigationSubmitButton freebirdThemedFilledButtonM2"]'

goBackLink = 'div[class="freebirdFormviewerViewResponseLinksContainer"]'
count = 0
browser = Browser()
while 1:
	url = "https://docs.google.com/forms/d/e/1FAIpQLSezT3kp25gmWqyneiGUgBeDuUyVf__m4bFVZHnFsVTsrB3-YQ/viewform?fbclid=IwAR0BI1pGjxZh0FcMGxJ-ADGEkB_Ru5lvhFC2vpE8omGnULUE2fjuFhWCYxs"
	browser.visit(url)
	divs = browser.find_by_css(button)
	divs.click()

	submit = browser.find_by_css(submitButton)
	submit.click()

	count = count + 1
	print(count)
	
			
