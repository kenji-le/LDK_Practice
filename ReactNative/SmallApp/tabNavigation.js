import { createBottomTabNavigator, createAppContainer } from 'react-navigation';
import About from './components/MH_About';
import Danh_sach_Android from './components/MH_Danh_sach_Android';
import Danh_sach_Iphone from './components/MH_Danh_sach_Iphone';
import Lien_he from './components/MH_Lien_he';

const routeConfigs = {
    
    Man_hinh_About:{
        screen:About
    },
    Man_hinh_Iphone:{
        screen:Danh_sach_Iphone
    },
    Man_hinh_Android:{
        screen:Danh_sach_Android
    },
    Man_hinh_Lien_he:{
        screen:Lien_he
    },
   
};
const tabNavigatorConfig = {
    initialRouterName:"Man_hinh_About",
    animationEnabled:true,
    swipeEnabled:true,
    tabBarOptions: {
        activeTintColor: 'tomato',
        inactiveTintColor: 'gray',
    },

    
};
const Man_hinh= createBottomTabNavigator(routeConfigs, tabNavigatorConfig);
const App=createAppContainer(Man_hinh);
export default App
 

