import { useState } from 'react';
function App() {
    // Создаем состояние: переменная text (текущий текст) и функция setText (для его изменения)
  const [text, setText] = useState("Нажми на кнопку, чтобы узнать секрет!");
  const handleClick = () => {
    setText("Секрет раскрыт! Ты станешь отличным фронтендером 🚀");
  };
  return (
    <div>
      <h1>Привет! Это мой первый интерактивный сайт</h1>
      
      {/* 3. Выводим текст из переменной через фигурные скобки */}
      <p>{text}</p> 
      
      {/* 4. Добавляем кнопку и привязываем к ней нашу функцию */}
      <button onClick={handleClick}>
        Нажми меня
      </button>
    </div>
  );
}

export default App;