import { GoogleButton } from "react-google-button";
import { hasLoggedIn, UserAuth } from "context/AuthContext";
import { useState, useEffect } from "react";
import { getAllUsers } from "api/firebase";
import Information from "components/Information";
import happy from "assets/images/happy.png";
import waiting from "assets/images/waiting.png";

export default function Login() {
  const { googleSignIn, user } = UserAuth();
  const [acceptedUser, setAcceptedUser] = useState(false);

  const handleGoogleSignIn = async () => {
    try {
      await googleSignIn();
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    getAllUsers()
      .then((allUsers) => {
        for (const someUser of allUsers) {
          if (someUser.email == user.email) {
            setAcceptedUser(someUser.accepted);
            break;
          }
        }
      })
      .catch((error) => console.log(error));
  }, [user]);

  if (!hasLoggedIn()) {
    return (
      <div>
        <GoogleButton onClick={handleGoogleSignIn} />
      </div>
    );
  }

  if (!acceptedUser) {
    return (
      <Information
        title={"Bienvenido, " + user.displayName.split(" ")[0] + "!"}
        text={
          <div style={{ textAlign: "center" }}>
            <p>Estás en la lista de espera!</p>
            <p>Ahora solamente falta que te acepte uno de nuestros admins!</p>
          </div>
        }
        img={waiting}
      />
    );
  } else {
    return (
      <Information
        title={"Bienvenido, " + user.displayName.split(" ")[0] + "!"}
        text={
          <div style={{ textAlign: "center" }}>
            <p>Ya has sido aceptado por nuestros admins!</p>
            <p>Ahora puedes aceptar contribuciones y a otros usuarios!</p>
          </div>
        }
        img={happy}
      />
    );
  }
}
