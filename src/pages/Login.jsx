import { GoogleButton } from "react-google-button";
import { UserAuth } from "context/AuthContext";

export default function Login() {
  const { googleSignIn } = UserAuth();

  const handleGoogleSignIn = async () => {
    try {
      await googleSignIn();
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div>
      <GoogleButton onClick={handleGoogleSignIn} />
    </div>
  );
}
