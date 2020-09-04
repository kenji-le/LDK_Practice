import React,{Component} from 'react';
import {View, Text,Image, FlatList, StyleSheet,TouchableOpacity} from 'react-native';
import Du_lieu from '../Xu_ly/Xu_ly_3L';
import {format_number} from '../Xu_ly/Dung_chung';
import Thong_tin_Dien_thoai from './MH_Thong_tin_Dien_thoai';

var url = "https://servicedatajs.herokuapp.com/";

class FlatListItem extends Component{ 
    XL_Chon(){
        this.props.navigation.navigate("Man_hinh_Thong_tin_Dien_thoai", {"Dien_thoai": this.props.item});
    }
    render(){
        return(
            <View style={{flex:1, flexDirection:"column"}}>
                <TouchableOpacity onPress={this.XL_Chon.bind(this)} activeOpacity={0.5}>
                    <View style={{flex:1, flexDirection:"row", backgroundColor: this.props.index % 2 ==0 ? "#e5f6ff":"#e5f6ff"}}>
                        <Image style={{height:80,width:120, margin:5}} source={{uri:(url + this.props.item.Ma_so + ".png")}}></Image>
                        <View style={{flex:1, flexDirection:"column", height:30}}>
                            <Text style={styles.itemText}>{this.props.item.Ten}</Text>
                            <Text style={styles.itemText}>Price: {format_number(this.props.item.Don_gia_Ban)} VND</Text>
                        </View>                
                    </View>
                    <View style={{height:1, backgroundColor:"#e6e5e5"}}></View>
                </TouchableOpacity>
            </View>
        );
    }
}

export default class Danh_sach_Android extends Component{
    static navigationOptions = ({navigation}) =>{
        let tabBarLabel= "Android";
        let tabBarIcon=()=>(
            <Image 
                source={require('../icons/android.png')} 
                style={{width:26, height:26}}/>
        );
        return {tabBarLabel, tabBarIcon};
    }

    constructor(props) {
        super(props);
        this.state = {dsDienThoai: Du_lieu};
    }

    componentDidMount() {
        fetch((url + "Danh_sach_Dien_thoai"), {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            }
        })
        .then((response) => response.json())
        .then((responseData) => {
            let dsAndroid = responseData.filter(item => {return item.Nhom_Dien_thoai.Ten == 'Android'});
            this.setState({dsDienThoai:dsAndroid});
        })
        .catch((error) => {
            console.log(error);
            alert(JSON.stringify(error));
        })
    }

    render(){        
        return (
            <View style={{marginTop:2}}>
                <FlatList 
                    data={this.state.dsDienThoai}
                    keyExtractor={(item) => item.Ma_so} 
                    renderItem={({item, index})=>{
                        return(
                            <FlatListItem item={item} index={index} navigation={this.props.navigation}></FlatListItem>
                        );
                    }}>
                </FlatList>        
            </View>
        );
    }
}

const styles= StyleSheet.create({
    itemText:{
        color:"#000000",
        padding:5,
        fontSize:14
    }
})


