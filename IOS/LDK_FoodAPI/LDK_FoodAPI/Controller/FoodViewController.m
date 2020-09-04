//
//  FoodViewController.m
//  LDK_FoodAPI
//
//  Created by LE DANG KHOA on 1/19/19.
//  Copyright © 2019 LDK. All rights reserved.
//

#import "FoodViewController.h"

@interface FoodViewController ()

@end

@implementation FoodViewController

@synthesize lblFood, imgFood, recipe;

- (void)viewDidLoad {
    [super viewDidLoad];
    [self setupView];
}

- (void)setupView {
    [lblFood setText:recipe.title];
    [lblFood setTextColor:[UIColor blueColor]];
    [lblFood sizeToFit];
    [lblFood setFrame:CGRectMake(0, STATUS_HEIGHT + NAVIGATION_HEIGHT, lblFood.frame.size.width, lblFood.frame.size.height)];
    [imgFood sd_setImageWithURL:[NSURL URLWithString:recipe.imageUrl] placeholderImage:[UIImage imageNamed:@"loading.png"]];
    [imgFood setFrame:CGRectMake(0, STATUS_HEIGHT + NAVIGATION_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT)];
    imgFood.contentMode = UIViewContentModeScaleAspectFit;
}

@end
