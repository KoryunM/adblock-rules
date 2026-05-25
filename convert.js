const fs = require('fs');
const { Converter } = require('@adguard/safari-converter');

// 1. Читаем скачанный текстовый файл (будет скачан скриптом позже)
const txtRules = fs.readFileSync('easylist.txt', 'utf8');

// 2. Конвертируем в формат Safari
const converter = new Converter({ advancedBlocking: true });
const result = converter.convert(txtRules);

// 3. Сохраняем как blockerList.json
fs.writeFileSync('blockerList.json', JSON.stringify(result, null, 2));
