from playwright.async_api import async_playwright

async def scrapping():
    async with async_playwright() as play:
        print("teste")
        browser = await play.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto('https://www.scrapethissite.com/pages/simple/')
        
        countries = await page.evaluate('''() => {
            const data = [...document.querySelectorAll('.col-md-4.country')];
            const countries = data.map(x => {
                const unifiedData = [
                    '.country-name',
                    '.country-population',
                    '.country-area'
                ];
                const [country, populationCount, areaKiloMeter] = unifiedData.map(arg => x.querySelector(arg).innerText);
                return {
                    country,
                    populationCount: Math.round(Number(populationCount)),
                    areaKiloMeters: Math.round(Number(areaKiloMeter)),
                    createdAt: new Date().toISOString()
                };
            });
            return countries;
        }''')
        await browser.close()
        return countries
