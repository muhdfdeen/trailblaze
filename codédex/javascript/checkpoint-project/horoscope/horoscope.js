const birthMonth = prompt('What is your birth month? ');
let zodiac = '';
let fortune = '';

if (birthMonth === 'January') {
    zodiac = 'Capricorn';
    fortune = 'A pleasant surprise awaits you!';
} else if (birthMonth === 'February') {
    zodiac = 'Aquarius';
    fortune = 'You will find peace in your surroundings.';
} else if (birthMonth === 'March') {
    zodiac = 'Pisces';
    fortune = 'Your creativity will shine this month.';
} else if (birthMonth === 'April') {
    zodiac = 'Aries';
    fortune = 'You will be filled with energy and enthusiasm.';
} else if (birthMonth === 'May') {
    zodiac = 'Taurus';
    fortune = 'You will find comfort in your routine.';
} else if (birthMonth === 'June') {
    zodiac = 'Gemini';
    fortune = 'Communication will be your strong suit this month.';
} else if (birthMonth === 'July') {
    zodiac = 'Cancer';
    fortune = 'You will be nurturing and protective of your loved ones.';
} else if (birthMonth === 'August') {
    zodiac = 'Leo';
    fortune = 'You will be confident and full of energy.';
} else if (birthMonth === 'September') {
    zodiac = 'Virgo';
    fortune = 'You will be analytical and detail-oriented.';
} else if (birthMonth === 'October') {
    zodiac = 'Libra';
    fortune = 'You will seek balance and harmony in your life.';
} else if (birthMonth === 'November') {
    zodiac = 'Scorpio';
    fortune = 'You will be passionate and determined.';
} else if (birthMonth === 'December') {
    zodiac = 'Sagittarius';
    fortune = 'You will be adventurous and open-minded.';
} else {
    fortune = 'Please enter a valid birth month.';
}

document.getElementById('fortune').textContent = `Your zodiac sign is ${zodiac}. ${fortune}`;