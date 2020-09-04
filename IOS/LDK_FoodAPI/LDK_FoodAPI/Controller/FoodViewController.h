//
//  FoodViewController.h
//  LDK_FoodAPI
//
//  Created by LE DANG KHOA on 1/19/19.
//  Copyright © 2019 LDK. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface FoodViewController : UIViewController

@property (weak, nonatomic) IBOutlet UIImageView *imgFood;
@property (weak, nonatomic) IBOutlet UILabel *lblFood;
@property (strong, nonatomic) Recipe *recipe;

@end
