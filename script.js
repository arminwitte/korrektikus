const originalText = document.getElementById('originalText');
const correctedText = document.getElementById('correctedText');
const submitButton = document.getElementById('submitButton');

submitButton.addEventListener('click', async () => {
  const text = originalText.value;

  if (!text) {
    alert('Please enter some text to correct');
    return;
  }

  const response = await fetch('https://api.bard.ai/v2/texts', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      text: text,
      language: 'de'
    })
  });

  const data = await response.json();
  correctedText.value = data.corrections[0];
});
