import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, TextInput, TouchableOpacity, View } from 'react-native';

export default function App() {
  return (
    <View style={styles.container}>
      <View> {/*container-image*/}
        <Image source={{ uri: "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Pok%C3%A9_Ball_icon.svg/2052px-Pok%C3%A9_Ball_icon.svg.png" }}
          widht={200}
          height={200}
        />
      </View>
      <View> {/*container-form*/}
        <Text style={styles.title}>Iniciar Sesión</Text>
        <Text style={styles.label}>Correo:</Text>
        <TextInput style={styles.input}/>
        <Text style={styles.label}>Contraseña</Text>
        <TextInput style={styles.input}/>
        <Pressable  style={styles.send}>
          <Text style={styles.textButton}>Enviar</Text>
        </Pressable>
      </View>
      <View> {/*container-footer*/}
        <Text style={styles.containerFooter}>¿Olvidaste tu contraseña?</Text>
        <Text style={styles.containerFooter}>Regístrate</Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    padding:10,
    alignItems: 'center',
    justifyContent: 'center',
  },
  title:{
    fontSize: 30,
    fontWeight: "bold"
  },
  label:{
    fontSize: 20,
    fontWeight: "bold"  
  },
  input:{
    borderRadius:10,
    borderWidth:2,
    fontSize: 15,
    borderColor: "black",
    width: "auto",
    backgroundColor: "blue"
  },
  send:{
    backgroundColor: "red",
    width: "auto",  
    height:"auto",
    borderRadius: 10,
    marginTop: 15,
    alignItems: "center",
    textButton:{
      color: "black",
      fontSize: 20,
      fontWeight: "bold"
    }
  },
  containerFooter:{
    justifyContent: "space-between",
    alignItems: "center",
    text:{
      fontSize: 20,
      margin:5
    }
  }
});
