import { useState } from 'react';

export default function App() {
  const [trainingDays, setTrainingDays] = useState(5);
  const [splitDays, setSplitDays] = useState({ push: 2, pull: 2, legs: 1 });
  const [exercisesPerDay, setExercisesPerDay] = useState({ push: 5, pull: 5, legs: 5 });

  const [proteinTarget, setProteinTarget] = useState(120);
  const [calorieTarget, setCalorieTarget] = useState(2200);
  const [proteinIntake, setProteinIntake] = useState(0);
  const [calorieIntake, setCalorieIntake] = useState(0);
  const [foodName, setFoodName] = useState('');
  const [proteinPerFood, setProteinPerFood] = useState('');
  const [caloriesPerFood, setCaloriesPerFood] = useState('');

  const pushExercises = [
    "🏋️ Bench Press",
    "🧍 Overhead Shoulder Press",
    "💪 Tricep Pushdown",
    "👐 Lateral Raises",
    "🧱 Dumbbell Chest Fly"
  ];
  const pullExercises = [
    "🏋️ Deadlift",
    "🏃 Pull-Ups / Chin-Ups",
    "🧲 Lat Pulldown",
    "💪 Barbell Curl",
    "🔁 Dumbbell Row"
  ];
  const legExercises = [
    "🏋️ Back Squat",
    "🦵 Leg Press",
    "🍑 Romanian Deadlift",
    "🦶 Calf Raises",
    "🚶 Walking Lunges"
  ];

  const handleSplitChange = (type, value) => {
    setSplitDays({ ...splitDays, [type]: parseInt(value) || 0 });
  };

  const handleExerciseChange = (type, value) => {
    setExercisesPerDay({ ...exercisesPerDay, [type]: parseInt(value) || 0 });
  };

  const handleAdd = () => {
    setProteinIntake((prev) => prev + parseFloat(proteinPerFood));
    setCalorieIntake((prev) => prev + parseFloat(caloriesPerFood));
    setFoodName('');
    setProteinPerFood('');
    setCaloriesPerFood('');
  };

  const handleImageUpload = (e) => {
    const file = e.target.files[0];
    alert("🧠 Image uploaded! (You can integrate food detection model here)");
  };

  return (
    <div style={{ padding: '2rem', fontFamily: 'Arial, sans-serif' }}>
      <h1>🏋️ PPL Gym Tracker + Protein Tracker</h1>

      <label>
        📅 Total Training Days/Week:
        <input
          type="number"
          value={trainingDays}
          onChange={(e) => setTrainingDays(parseInt(e.target.value) || 0)}
        />
      </label>

      <h2 style={{ marginTop: '1rem' }}>🧩 PPL Split</h2>
      {['push', 'pull', 'legs'].map((type) => (
        <div key={type}>
          <label>
            {type.charAt(0).toUpperCase() + type.slice(1)} Days:
            <input
              type="number"
              value={splitDays[type]}
              onChange={(e) => handleSplitChange(type, e.target.value)}
            />
          </label>
          <label style={{ marginLeft: '1rem' }}>
            Exercises/Day:
            <input
              type="number"
              value={exercisesPerDay[type]}
              onChange={(e) => handleExerciseChange(type, e.target.value)}
            />
          </label>
        </div>
      ))}

      <h2>✅ Recommended Exercises</h2>
      <div>
        <h3>Push Day (Chest, Triceps, Shoulders)</h3>
        <ul>{pushExercises.slice(0, exercisesPerDay.push).map((ex, idx) => <li key={idx}>{ex}</li>)}</ul>
        <h3>Pull Day (Back, Biceps)</h3>
        <ul>{pullExercises.slice(0, exercisesPerDay.pull).map((ex, idx) => <li key={idx}>{ex}</li>)}</ul>
        <h3>Leg Day (Quads, Hamstrings, Glutes)</h3>
        <ul>{legExercises.slice(0, exercisesPerDay.legs).map((ex, idx) => <li key={idx}>{ex}</li>)}</ul>
      </div>

      <hr style={{ margin: '2rem 0' }} />

      <h2>🍗 Protein & Calorie Tracker</h2>
      <label>
        🎯 Protein Target (g):
        <input type="number" value={proteinTarget} onChange={(e) => setProteinTarget(parseFloat(e.target.value))} />
      </label><br/>
      <label>
        🔥 Calorie Target (kcal):
        <input type="number" value={calorieTarget} onChange={(e) => setCalorieTarget(parseFloat(e.target.value))} />
      </label>

      <h3 style={{ marginTop: '1rem' }}>📝 Manual Entry</h3>
      <label>Food Name: <input value={foodName} onChange={(e) => setFoodName(e.target.value)} /></label><br/>
      <label>Protein (g): <input value={proteinPerFood} onChange={(e) => setProteinPerFood(e.target.value)} /></label><br/>
      <label>Calories (kcal): <input value={caloriesPerFood} onChange={(e) => setCaloriesPerFood(e.target.value)} /></label><br/>
      <button onClick={handleAdd}>➕ Add</button>

      <h3>📸 Upload Meal Image</h3>
      <input type="file" accept="image/*" capture="environment" onChange={handleImageUpload} />

      <h3>📊 Daily Progress</h3>
      <p>Protein: {proteinIntake}g / {proteinTarget}g</p>
      <progress value={proteinIntake} max={proteinTarget}></progress><br/>
      <p>Calories: {calorieIntake} kcal / {calorieTarget} kcal</p>
      <progress value={calorieIntake} max={calorieTarget}></progress>
    </div>
  );
}
