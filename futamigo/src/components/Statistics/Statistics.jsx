import { useEffect, useState } from "react";
import axios from 'axios';
import manchester_united from '/src/assets/manchester_united.png';
import manchester_city from '/src/assets/manchester_city.png';
import real_madrid from '/src/assets/real_madrid.jpg';
import real_sociedad from '/src/assets/real_sociedad.png';

const Statistics = () => {
    const [data, setData] = useState([]);
    const logos = {
        real_madrid: real_madrid,
        real_sociedad: real_sociedad,
        manchester_city: manchester_city,
        manchester_united: manchester_united
    };

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:5000/statistics');
                setData(response.data);
            } catch (error) {
                console.error("Fetching data error: ", error);
            }
        };

        fetchData();
    }, []);

    const handleClick = (item) => {
        console.log(itedatm)
    }

    return (
        <table className="result-table">
            <thead>
                <tr>
                    <th>Home Team</th>
                    <th>Visitor Team</th>
                    <th>Result</th>
                    <th>Date</th>
                </tr>
            </thead>
            <tbody>
                {data.length > 0 ? (
                    data.map((item, index) => (
                        <tr 
                            key={index}
                            onClick={() => handleClick(item)}
                        >
                            <td>{item.home_team} <img src={logos[item.home_team.toLowerCase().replace(' ', '_')]} alt={`${item.home_team} logo`} /></td>
                            <td>{item.visitor_team} <img src={logos[item.visitor_team.toLowerCase().replace(' ', '_')]} alt={`${item.visitor_team} logo`} /></td>
                            <td>{item.result}</td>
                            <td>4/20/2020</td>
                        </tr>
                    ))
                ) : (
                    <tr>
                        <td colSpan={3}>Loading...</td>
                    </tr>
                )}
            </tbody>
        </table>
    );
};

export default Statistics;
