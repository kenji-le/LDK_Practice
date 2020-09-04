import React, {Component} from 'react';
import {Image, Text, View} from 'react-native';

const backgroundColor="blue";
export default class Lien_he extends Component{
    static navigationOptions = ({navigation}) =>{
        const {params = {}} = navigation.state;
        let tabBarLabel= "Liên hệ";
        let tabBarIcon=()=>(
            <Image source={require('../icons/customer.png')} style={{width:26, height:26, tintColor:backgroundColor}}/>
        );
        return {tabBarLabel, tabBarIcon};
    }
    render(){
        return(
            <View style={{flex:1, backgroundColor:backgroundColor, justifyContent:'center', alignItems:'center'}}>
                <Image style={{height:80,width:120, margin:5}} source={require('../images/PET.png')}></Image>
            </View>
        );
    }
}