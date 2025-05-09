import { type ChangeEvent } from 'react';
import axios from 'axios';

function App() {
  const handleImageUpload = async (e: ChangeEvent<HTMLInputElement>) => {
    const image = e.target.files?.[0];

    if (!image) return;

    const formData = new FormData();
    formData.append('image', image);

    try {
      const response = await axios.post(
        'http://localhost:8000/image',
        formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        },
      );

      console.log(response.data);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div className="w-screen h-screen flex items-center justify-center">
      <div>
        <label htmlFor="img">Upload Image</label>
        <input name="img" type="file" onChange={handleImageUpload} />
      </div>
    </div>
  );
}

export default App;
