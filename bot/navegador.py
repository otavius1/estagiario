from playwright.async_api import async_playwright

async def abrir_site():
    playwright = await async_playwright().start()
    browser = await playwright.chromium.launch(headless=False)
    page = await browser.new_page()
    await page.goto("https://pje-consultapublica.tjdft.jus.br/consultapublica/ConsultaPublica/listView.seam")
    return playwright, browser, page

async def consultar_processo(page, numero_processo):
    await page.fill(
        '#fPP\\:numProcesso-inputNumeroProcessoDecoration\\:numProcesso-inputNumeroProcesso',
        numero_processo
    )
    await page.locator("text=Pesquisar").click()
    await page.wait_for_selector('a[title="Ver Detalhes"]')

    new_page_future = page.context.wait_for_event("page")
    await page.click('a[title="Ver Detalhes"]')
    nova_aba = await new_page_future
    await nova_aba.wait_for_load_state('networkidle')
    return nova_aba
