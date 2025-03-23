fetch('data/phrases.json')
  .then(res => res.json())
  .then(data => {
    const container = document.getElementById('player-container');

    data.forEach(entry => {
      const card = document.createElement('div');
      card.classList.add('card');

      const en = document.createElement('p');
      en.textContent = `🇺🇸 ${entry.english}`;
      card.appendChild(en);

      const ru = document.createElement('p');
      ru.textContent = `🇷🇺 ${entry.russian}`;
      card.appendChild(ru);

      const expl = document.createElement('p');
      expl.textContent = `🧠 ${entry.explanation_en || ''} ${entry.explanation_ru || ''}`;
      card.appendChild(expl);

      const audio = document.createElement('audio');
      audio.controls = true;
      audio.src = entry.filename;
      card.appendChild(audio);

      container.appendChild(card);
    });
  })
  .catch(err => {
    console.error("Failed to load phrases.json:", err);
  });


