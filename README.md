# Japanese Pokémon Card Profit Finder

This Python project compares Japanese Pokémon card prices listed in a Google Sheet (or Excel file) against TCGplayer market prices to identify cards that could be resold for profit.

By automating price lookups and profit calculations, the script helps collectors and resellers quickly find undervalued cards in the Japanese market.

---

## Features

- **Automated Price Scraping** — Uses Selenium to search TCGplayer and fetch real-time card prices.  
- **Spreadsheet Integration** — Reads Japanese Pokémon card data from a spreadsheet (`JPNpoke.xlsx`).  
- **Profit Calculation** — Compares Japanese card prices to TCGplayer prices to find potential profit margins.  
- **Output Reports** — Exports results to:
  - `buySheet.xlsx` — Cards that are profitable.
  - `checkSheet.xlsx` — Cards that could not be matched or found on TCGplayer.

---

## Requirements

Install dependencies:

```bash
pip install pandas selenium webdriver-manager openpyxl
```

You also need:
- Google Chrome (latest version)
- ChromeDriver (automatically managed by `webdriver-manager`)

---

## Input Format

The script expects an Excel file named `JPNpoke.xlsx` with the following columns:

| name | usd |
|------|-----|
| Pikachu {001/100}〈Set Name〉 | 12.34 |

- **name**: Pokémon card name, set number, and set name (formatted as shown)  
- **usd**: Price in USD from the Japanese market  

---

## How to Run

1. Place your `JPNpoke.xlsx` file in the same folder as `Main.py`.  
2. Run the script:

```bash
python Main.py
```

3. Wait while Selenium scrapes TCGplayer for each card’s price.  
4. Check the generated output files:
   - `buySheet.xlsx` — profitable cards  
   - `checkSheet.xlsx` — cards not found or out of stock  

---

## Profit Logic

A card is marked **profitable** if:
- The TCGplayer price is at least 30% lower than the Japanese price, **or**
- The TCGplayer price is $10 lower than the Japanese price.  

---

## Example Output

When a profitable card is found, the script prints details to the console:

```
Pikachu VMAX $20.00 Profit: $8.50
```

---

## Notes

- TCGplayer’s site structure may change, which could affect scraping reliability.  
- The script assumes English and Japanese cards share identical set numbering formats.  
- For large spreadsheets, consider increasing Selenium’s wait time for stability.  

---

## Future Improvements

- Integrate directly with the Google Sheets API.  
- Implement asynchronous scraping for faster performance.  
- Add automatic currency conversion and historical trend analysis.  

---

## License

This project is released under the MIT License.
