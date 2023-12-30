var text =
  "Cyber Law is." +
  "An Advance fake news detection system could be a significant step and has wide-ranging outcomes.";
("It will be promoting accurate reporting, improving media literacy,");
("and reducing the spread of fake news and disinformation");

function autoType() {
  var element = document.getElementById("auto-typing");
  var index = 0;
  setInterval(function () {
    element.innerHTML = text.substr(0, index);
    index++;
  }, 100);
}

// <script>
//   // Define a function to fetch the temperature data
//   function fetchTemperature() {
//     API_KEY = "c3714d446c4d48d1910122040232903";
//     const location = "Phagwara";

//     axios
//       .get(
//         `https://api.weatherapi.com/v1/current.json?key=${API_KEY}&q=${location}`
//       )
//       .then((response) => {
//         temperature = response.data.current.temp_c;

//         // Set the temperature value to the state
//         setTemp(temperature);
//       });
//   }

//   // Call the fetchTemperature function when the component mounts
//   useEffect(() => {
//     fetchTemperature();
//   }, []);

//   // Create a reference to the element that will display the typed text
//   const el = useRef(null);

//   // Call the Typed constructor to create the typed effect
//   useEffect(() => {
//     let typed = new Typed(el.current, {
//       strings: [
//         '"Disinformation is the brainchild of a self-absorbed Behaviour." ',
//         '"An Advance fake news detection system could be a significant step and has wide-ranging outcomes."',
//         '"It will be promoting accurate reporting, improving media literacy,"',
//         '" and reducing the spread of fake news and disinformation"',
//       ],
//       typeSpeed: 20,
//       smartBackspace: true,
//       startDelay: 1000,
//       shuffle: false,
//       loop: true,
//       loopCount: Infinity,
//     });

//     // Call the destroy method to remove the typed effect when the component unmounts
//     return () => {
//       typed.destroy();
//     };
//   {">"}, []);

//   // Define a state to hold the temperature value
//   const [temp, setTemp] = useState(null);

//   // Render the temperature value and the typed text
//   return (
//     <div>
//       <p>Temperature: {temp}</p>
//       <p ref={el}></p>
//     </div>
//   );
// </script>
