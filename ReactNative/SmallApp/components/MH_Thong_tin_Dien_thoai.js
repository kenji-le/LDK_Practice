
import React, {Component} from 'react';
import {View,Image, TouchableOpacity,Text, TextInput,StyleSheet, ToastAndroid} from 'react-native';
import Du_lieu from '../Xu_ly/Xu_ly_3L';

var url = "https://servicedatajs.herokuapp.com/";

export default class Thong_tin_Dien_thoai extends Component{
  
    static navigationOptions = ({ navigation }) => {
        return {
            title: navigation.getParam('Dien_thoai').Ten,
            headerStyle: {
                backgroundColor: '#e5f6ff',
            },
            headerTintColor: '#4387fd',
            headerTitleStyle: {
                fontWeight:"normal",
                fontSize:16
            }
        };
    };

    constructor(props) {
        super(props);
        let Dien_thoai = this.props.navigation.state.params.Dien_thoai;
        this.state = {
            Ma_so: Dien_thoai.Ma_so,
            Ten: Dien_thoai.Ten,
            Don_gia_Ban: Dien_thoai.Don_gia_Ban,
            Ket_qua: ""
        }
    }

    XL_Nhan() {
        if (this.state.Don_gia_Ban != "") {
            let Ma_so = this.state.Ma_so;
            let Dien_thoai = Du_lieu.Danh_sach_Dien_thoai.find(item =>item.Ma_so == Ma_so);
            fetch((url + 'Cap_nhat_Dien_thoai'), {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    Ma_so: Dien_thoai.Ma_so,
                    Don_gia_Ban:parseFloat(this.state.Don_gia_Ban),
                })
            })
            .then((response) => response.json()
            )
            .then((responseData) => {
                if(responseData.Noi_dung==1){
                    Dien_thoai.Don_gia_Ban=parseFloat(this.state.Don_gia_Ban);
                    this.props.navigation.state.params.Doi_tuong.refreshFlatListItem();
                    this.props.navigation.goBack();
                }                              
            })
            .catch((error) => {
                console.log(error);
            })          
            
        }            
        else
            alert('Lỗi cập nhật');     
       
    }

    render(){
        //const { navigate } = this.props.navigation;                     
        return(                 
            <View style={style.container}>
                <View style={{alignItems:"center",marginTop:20}}>
                    <Image style={style.image} source={{uri:url + this.state.Ma_so + '.png'}}></Image>  
                </View> 
                <View style={{flex:1, justifyContent:"flex-start"}}>
                    <TextInput onChangeText={(Ma_so)=>this.setState({Ma_so})} value={this.state.Ma_so} placeholder='Mã số' style={style.input}/>
                    <TextInput onChangeText={(Ten)=>this.setState({Ten})} value={this.state.Ten} placeholder='Tên' style={style.input}/>
                    <TextInput onChangeText={(Don_gia_Ban)=>this.setState({Don_gia_Ban})} value={this.state.Don_gia_Ban.toString()} placeholder='Đơn giá' style={style.input} />                
                    <TouchableOpacity onPress={this.XL_Nhan.bind(this)} activeOpacity={0.5}>
                        <View style={style.button}>
                            <Text style={style.text}>Cập nhật</Text>
                        </View>
                    </TouchableOpacity>   
                </View>          
            </View>          
        );        
    }
}

const style= StyleSheet.create({
    container:{
      flex:1,
      backgroundColor:'#e5f6ff',
      justifyContent:'center'
    },
    input:{
      paddingHorizontal:10,
      backgroundColor:'#ffffff',
      margin:5,
      borderRadius:5
    },
    button:{
      height:46,
      borderRadius:5,
      margin:5,
      backgroundColor:'#4387fd',
      justifyContent:'center',
      alignItems:'center'
    },
    text:{
      color:'#ffffff',
      fontSize:16,
    },
    image:{
        height:160,
        width:240,
        marginBottom:20,
        borderTopLeftRadius:10,
        borderTopRightRadius:10,
        borderBottomLeftRadius:10,
        borderBottomRightRadius:10
    }
  })