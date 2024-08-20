import './App.css';
import { useState } from 'react';
import axios from 'axios';
import Diabetes_Detection_logo from './Diabetes_Detection_logo.jpg'
function App() {
  const [features, setFeatures] = useState({
    feature1: 2,
    feature2: 107,
    feature3: 74,
    feature4: 30,
    feature5: 100,
    feature6: 24.6,
    feature7: 0.404,
    feature8: 23
    // Add all the features your model requires
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFeatures({
      ...features,
      [name]: value
    });
  };

  const [prediction, setPrediction] = useState("Fill the Above Values");

  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log("hello");
    try {
        const response = await axios.post('https://diabetes-detection-system.onrender.com', {
            features: Object.values(features).map(Number)
        });
        const prediction = response.data.prediction;
        console.log(prediction);
        setPrediction(prediction); // Set the state if needed elsewhere
        alert('You are ' + prediction);
    } catch (err) {
        console.error("There was an error making the request:", err.message || err);
        alert('Failed to fetch data. Please check the server.');
    }
};


  return (
    <div className="App">
      <form  className='flex flex-col items-center w-[80%] h-[90vh] rounded-[30px] m-auto my-[2%]  justify-center border-[4px] border-green-300 ' onSubmit={handleSubmit}>
        <img className=' w-[80%] h-[18vw] mb-[30px] rounded-[39px]' src={Diabetes_Detection_logo} alt="Logo" />
      <h1 className='text-[40px] my-[10px]  font-serif'> Diabetics Detection App</h1>
        <div className='flex items-center justify-center gap-5'>
        <div >Pregnancies<input  className='pl-[20px] w-[100px] border-[2px] border-black-300'type="number" name="feature1" value={features.feature1} onChange={handleChange} /></div>
        <div>Glucose: <input  className='pl-[20px] w-[100px] border-[2px] border-black-300'type="number" name="feature2" value={features.feature2} onChange={handleChange} /></div>
        <div>BloodPressure: <input  className='pl-[20px] w-[100px] border-[2px] border-black-300'type="number" name="feature3" value={features.feature3} onChange={handleChange} /></div>
        <div>SkinThickness: <input  className='pl-[20px] w-[100px] border-[2px] border-black-300'type="number" name="feature4" value={features.feature4} onChange={handleChange} /></div>
        <div>Insulin: <input className='pl-[20px] w-[100px] border-[2px] border-black-300' type="number" name="feature5" value={features.feature5} onChange={handleChange} /></div>
        <div>BMI: <input  className='pl-[20px] w-[100px] border-[2px] border-black-300'type="number" name="feature6" value={features.feature6} onChange={handleChange} /></div>
        <div>DiabetesPedigreeFunction: <input  className='pl-[20px] w-[100px] border-[2px] border-black-300'type="number" name="feature7" value={features.feature7} onChange={handleChange} /></div>
        <div>Age: <input  className='pl-[20px] w-[100px] border-[2px] border-black-300 mr-[10px]' type="number" name="feature8" value={features.feature8} onChange={handleChange} /></div>
        </div>
        <button type='submit' className='my-[30px] bg-green-500 text-white rounded-[20px] w-[200px] '>Submit</button>
      <div className='text-[30px] text-mono  flex justify-center '>Result: <div className='mx-[10px] text-blue-600'>{prediction}</div></div>
      </form>
    </div>
  );
}

export default App;
