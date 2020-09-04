import React, {Component} from 'react';
import {Image, Text, View} from 'react-native';

const backgroundColor="#0067a7";
export default class About extends Component{
    static navigationOptions = ({navigation}) =>{
        let tabBarLabel= "About";
        let tabBarIcon=()=>(
            <Image 
                source={require('../icons/home.png')} 
                style={{width:26, height:26, tintColor:backgroundColor}}/>
        );
        return {tabBarLabel, tabBarIcon};
    }
    
    render(){
        return(
            <View style={{flex:1, backgroundColor:backgroundColor, justifyContent:'center', alignItems:'center'}}>
                <Text style={{fontWeight:"bold", fontSize:22 ,color:"#ffffff"}}>
                    Name: Le Dang Khoa
                </Text>
                <Text style={{fontWeight:"bold", fontSize:22 ,color:"#ffffff"}}>
                    Class: React Native
                </Text>         
            </View>
        );
    }
}