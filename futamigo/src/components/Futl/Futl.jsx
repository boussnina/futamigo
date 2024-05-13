import { useEffect, useState } from "react";
import axios from 'axios';


const Futl = () => {
    const [answer, setAnswer] = useState([])
    const [input, setInput] = useState("")
    const [suggestions, setSuggestions] = useState ([])
    const [guesses, setGuesses] = useState([
        { name: "Livramento", age: 22, position: "Defender", country: "England", titles: 0 },
    ]);


    useEffect(() => {
        //Lav kald til database, og find en random spiller.
        //request /getRando
        // setAnswer(response.data)
        console.log("INPUT ÆNDRTET")
    }, [input])

    const handleChange = (textInput) => {
        setInput(textInput)
        const fetchData = async () => {
            if (textInput.length > 0){
                try {
                    const response = await axios.get(`http://127.0.0.1:5000/futl/${textInput}`);
                    setSuggestions(response.data);
                } catch (error) {
                    console.error("Fetching data error: ", error);
                }
            }
            else {
                setSuggestions([]);
            }
        };

        fetchData();
        // console.log(suggestions)
        //Herefter skal den lave kald til db, og
        //finde fodboldspillere hvis navn indeholder bogstaverne
        //Så der kan komme suggestions
    }

    const handleSubmit = (playerGuess) => {
        console.log(playerGuess)
        var player = { name: playerGuess, age: 0, position: "Bench", country: "Unknown", titles: 0}
        setGuesses((prev) => [...prev, player]);
        //Skal tjekke om det er en valid fodboldspiller fra db
        //Hvis ja, er den spiller du har fået retur === answer,
        //Hvis ja, har du vundet.
        
    }

    return (
        <>
            <div className="futl-game">
                <div className="inputs">
                    <input
                        value={input}
                        onChange={(e) => handleChange(e.target.value)}
                        placeholder="Guess the player"
                    />
                    <button onClick={() => handleSubmit(input)}>Submit</button>
                </div>
                {suggestions.length > 0 && (
                    <ul className="suggestions">
                        {suggestions.map((suggestion, index) => (
                        <li key={index} onClick={() => {
                            setInput(suggestion.name); // Update the input with the player's name
                            setSuggestions([]); // Clear the suggestions
                        }}>
                            {suggestion.name} - {suggestion.club}
                        </li>
                        ))}
                    </ul>
                )}
                <table>
                    <thead>
                        <tr>
                            <th>Name</th>
                            <th>Age</th>
                            <th>Position</th>
                            <th>Country</th>
                            <th>Titles</th>
                        </tr>
                    </thead>
                    <tbody>
                        {guesses.map((player, index) => (
                            <tr key={index}>
                                <td>{player.name}</td>
                                <td>{player.age}</td>
                                <td>{player.position}</td>
                                <td>{player.country}</td>
                                <td>{player.titles}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
            <div className="button1"></div>
            <div className="button2"></div>
        </>
    )
}

export default Futl;
