//
//  FoodWebViewController.h
//  LDK_FoodAPI
//
//  Created by LE DANG KHOA on 1/22/19.
//  Copyright © 2019 LDK. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface FoodWebViewController : UIViewController

@property (weak, nonatomic) IBOutlet UIWebView *webView;
@property (strong, nonatomic) Recipe *inputFood;

@end
