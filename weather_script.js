const apiKey = '888ae371c0f61f55971d752c22733538'; // Replace with your OpenWeatherMap API key

        document.getElementById('getWeather').addEventListener('click', async () => {
            const city = document.getElementById('city').value;
            if (!city) {
                alert('Please enter a city name.');
                return;
            }

            const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

            try {
                const response = await fetch(url);
                if (!response.ok) {
                    throw new Error('City not found', response.status);
                }

                const data = await response.json();
                const weather = `
                    <h2>Weather in ${data.name}</h2>
                    <p>Temperature: ${data.main.temp}°C</p>
                    <p>Weather: ${data.weather[0].description}</p>
                    <p>Humidity: ${data.main.humidity}%</p>
                    <p>Wind Speed: ${data.wind.speed} m/s</p>
                `;
                document.getElementById('weatherResult').innerHTML = weather;
            } catch (error) {
                document.getElementById('weatherResult').innerHTML = `<p>Error: ${error.message}</p>`;
            }
        });